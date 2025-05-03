// Please install OpenAI SDK first: `npm install openai`

import OpenAI, { AuthenticationError, APIError } from 'openai';
import dotenv from 'dotenv';
dotenv.config();

console.log(process.env.API_KEY);
console.log(process.env.API_BASE_URL);

const openai = new OpenAI({
  baseURL: process.env.API_BASE_URL,
  apiKey: process.env.API_KEY,
});

async function main() {
  try {
    const completion = await openai.chat.completions.create({
      messages: [{ role: 'system', content: 'You are a helpful assistant.' }],
      model: 'deepseek-chat',
    });
    console.log(completion.choices[0].message.content);
  } catch (err) {
    if (err instanceof AuthenticationError) {
      console.error('authentication failed', err.message);
    }
    if (err instanceof APIError) {
      console.error('api error', err.message);
    }
    if (err instanceof Error) {
      console.error('general err', err.message);
    } else {
      console.error('unknown error');
    }
  }
}

main();
