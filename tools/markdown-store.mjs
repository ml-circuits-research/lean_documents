/** Readable, schema-specific example metadata. No embedded data serialization. */
import { readFile, writeFile, rename, unlink } from 'node:fs/promises';
import { randomUUID } from 'node:crypto';

const allowed = new Set(['schema_version', 'title', 'description', 'question', 'reports', 'source_directory', 'brief', 'introductory', 'file_names', 'language']);
const headings = new Map([
  ['Description', 'description'], ['Review question', 'question'],
  ['Source directory', 'source_directory'], ['Review brief', 'brief'],
  ['Introductory example', 'introductory'], ['Reports', 'reports'],
  ['Format version', 'schema_version'], ['Original filenames', 'file_names'],
  ['Document language', 'language'],
]);

function prose(value, field, allowEmpty = false) {
  if (typeof value !== 'string' || (!allowEmpty && !value.trim()) || value !== value.trim() || /\r/.test(value) || /^#{1,2}\s/m.test(value)) {
    throw new Error(`${field} must be text without leading/trailing whitespace or reserved level-one/level-two headings (use level-three headings within prose)`);
  }
  return value;
}

function validate(data) {
  if (!data || typeof data !== 'object' || Array.isArray(data)) throw new Error('Example metadata must be an object');
  for (const key of Object.keys(data)) if (!allowed.has(key)) throw new Error(`Unknown example field: ${key}`);
  if (data.schema_version !== 1) throw new Error('Example format version must be 1');
  for (const key of ['title', 'source_directory']) prose(data[key], key);
  for (const key of ['description', 'question']) prose(data[key], key, true);
  if (Object.hasOwn(data, 'language') && !['en', 'ro'].includes(data.language)) throw new Error('language must be en or ro');
  if (data.title.includes('\n')) throw new Error('Example title must use one line');
  if (Object.hasOwn(data, 'brief')) prose(data.brief, 'brief');
  if (Object.hasOwn(data, 'introductory') && typeof data.introductory !== 'boolean') throw new Error('introductory must be boolean');
  if (!Array.isArray(data.reports)) throw new Error('reports must be an array (empty is allowed during creation)');
  if (Object.hasOwn(data, 'file_names')) {
    if (!data.file_names || typeof data.file_names !== 'object' || Array.isArray(data.file_names)) throw new Error('file_names must map file paths to original names');
    for (const [path, name] of Object.entries(data.file_names)) {
      prose(path, 'stored file path');
      prose(name, 'original file name');
    }
  }
  for (const report of data.reports) {
    if (!report || typeof report !== 'object' || Object.keys(report).some(key => !['path', 'label'].includes(key))) throw new Error('Reports require only path and label');
    prose(report.path, 'report path');
    prose(report.label, 'report label');
  }
  return data;
}

// Standard HTML entities keep literal pipes from breaking Markdown tables.
function cell(value) {
  return value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
    .replaceAll('|', '&#124;').replaceAll('\n', '<br>');
}
function uncell(value) {
  return value.replaceAll('<br>', '\n').replaceAll('&#124;', '|').replaceAll('&gt;', '>')
    .replaceAll('&lt;', '<').replaceAll('&amp;', '&');
}

export function formatExample(metadata) {
  const data = validate(metadata);
  const sections = [`# ${data.title}`, `## Description\n\n${data.description}`,
    `## Review question\n\n${data.question}`, `## Source directory\n\n${data.source_directory}`];
  if (Object.hasOwn(data, 'language')) sections.push(`## Document language\n\n${data.language === 'ro' ? 'Romanian' : 'English'}`);
  if (Object.hasOwn(data, 'brief')) sections.push(`## Review brief\n\n${data.brief}`);
  if (Object.hasOwn(data, 'introductory')) sections.push(`## Introductory example\n\n${data.introductory ? 'Yes' : 'No'}`);
  sections.push('## Reports\n\n| Report | File |\n| --- | --- |\n' + data.reports.map(report => `| ${cell(report.label)} | ${cell(report.path)} |`).join('\n'));
  if (Object.hasOwn(data, 'file_names')) sections.push('## Original filenames\n\n| File | Original name |\n| --- | --- |\n' + Object.entries(data.file_names).map(([path, name]) => `| ${cell(path)} | ${cell(name)} |`).join('\n'));
  sections.push(`## Format version\n\n${data.schema_version}`);
  return sections.join('\n\n') + '\n';
}

export function parseExample(markdown) {
  if (typeof markdown !== 'string') throw new Error('Example document must be text');
  const lines = markdown.replaceAll('\r\n', '\n').trim().split('\n');
  const title = /^# (.+)$/.exec(lines.shift() || '');
  if (!title) throw new Error('Example document must begin with its title');
  const data = { title: title[1] };
  let current = null;
  const sections = new Map();
  for (const line of lines) {
    const heading = /^## (.+)$/.exec(line);
    if (heading) {
      current = headings.get(heading[1]);
      if (!current) throw new Error(`Unknown example section: ${heading[1]}`);
      if (sections.has(current)) throw new Error(`Duplicate example section: ${heading[1]}`);
      sections.set(current, []);
    } else if (current) sections.get(current).push(line);
    else if (line.trim()) throw new Error('Unexpected text before example sections');
  }
  for (const [key, body] of sections) {
    const text = body.join('\n').trim();
    if (key === 'reports') {
      const rows = text.split('\n');
      if (!/^\|\s*Report\s*\|\s*File\s*\|$/.test(rows[0] || '') || !/^\|\s*:?-+:?\s*\|\s*:?-+:?\s*\|$/.test(rows[1] || '')) {
        throw new Error('Reports must be a table with Report and File columns');
      }
      data.reports = rows.slice(2).map(row => {
        const match = /^\|([^|]*)\|([^|]*)\|$/.exec(row);
        if (!match) throw new Error('Invalid report table row');
        return { label: uncell(match[1].trim()), path: uncell(match[2].trim()) };
      });
    } else if (key === 'file_names') {
      const rows = text.split('\n');
      if (!/^\|\s*File\s*\|\s*Original name\s*\|$/.test(rows[0] || '') || !/^\|\s*:?-+:?\s*\|\s*:?-+:?\s*\|$/.test(rows[1] || '')) throw new Error('Original filenames must be a table with File and Original name columns');
      const entries = rows.slice(2).map(row => {
        const match = /^\|([^|]*)\|([^|]*)\|$/.exec(row);
        if (!match) throw new Error('Invalid original filename row');
        return [uncell(match[1].trim()), uncell(match[2].trim())];
      });
      if (new Set(entries.map(([path]) => path)).size !== entries.length) throw new Error('Duplicate stored file path');
      data.file_names = Object.fromEntries(entries);
    } else if (key === 'schema_version') {
      if (text !== '1') throw new Error('Example format version must be 1');
      data.schema_version = 1;
    } else if (key === 'language') {
      if (!['English', 'Romanian'].includes(text)) throw new Error('Document language must be English or Romanian');
      data.language = text === 'Romanian' ? 'ro' : 'en';
    } else if (key === 'introductory') {
      if (!['Yes', 'No'].includes(text)) throw new Error('Introductory example must be Yes or No');
      data.introductory = text === 'Yes';
    } else data[key] = text;
  }
  return validate(data);
}

export async function readExample(path) {
  try {
    return parseExample(await readFile(path, 'utf8'));
  } catch (error) {
    if (error.code === 'ENOENT') return null;
    throw error;
  }
}

export async function writeExample(path, metadata) {
  const text = formatExample(metadata);
  const temporary = `${path}.${randomUUID()}.tmp`;
  try {
    // Same-directory rename makes catalog readers see one complete version.
    await writeFile(temporary, text, { encoding: 'utf8', flag: 'wx' });
    await rename(temporary, path);
  } finally {
    await unlink(temporary).catch(error => { if (error.code !== 'ENOENT') throw error; });
  }
}
