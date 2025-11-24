'use server';
/**
 * @fileOverview An AI-powered tool to diagnose car issues through a conversational interface.
 *
 * - diagnoseIssue - A function that handles the car issue diagnosis process.
 * - DiagnoseIssueInput - The input type for the diagnoseIssue function.
 * - DiagnoseIssueOutput - The return type for the diagnoseIssue function.
 */

import {ai} from '@/ai/genkit';
import {z} from 'genkit';

const DiagnoseIssueInputSchema = z.object({
  issueDescription: z.string().describe('A description of the car issue provided by the user.'),
  conversationHistory: z.array(z.object({
    role: z.enum(['user', 'assistant']),
    content: z.string(),
  })).optional().describe('The conversation history between the user and the assistant.'),
});
export type DiagnoseIssueInput = z.infer<typeof DiagnoseIssueInputSchema>;

const DiagnoseIssueOutputSchema = z.object({
  diagnosis: z.string().describe('The diagnosis of the car issue.'),
  relevantDataPoints: z.array(z.string()).describe('A list of relevant data points to record for the mechanics.'),
});
export type DiagnoseIssueOutput = z.infer<typeof DiagnoseIssueOutputSchema>;

export async function diagnoseIssue(input: DiagnoseIssueInput): Promise<DiagnoseIssueOutput> {
  return diagnoseIssueFlow(input);
}

const prompt = ai.definePrompt({
  name: 'diagnoseIssuePrompt',
  input: {schema: DiagnoseIssueInputSchema},
  output: {schema: DiagnoseIssueOutputSchema},
  prompt: `You are an AI-powered tool that helps users diagnose their car issues through a conversational interface.

You will take the issue description and conversation history (if any) as input, and provide a diagnosis of the car issue and a list of relevant data points to record for the mechanics.

Issue Description: {{{issueDescription}}}

Conversation History:
{{#each conversationHistory}}
{{role}}: {{{content}}}
{{/each}}

Diagnosis:
Relevant Data Points:`, 
});

const diagnoseIssueFlow = ai.defineFlow(
  {
    name: 'diagnoseIssueFlow',
    inputSchema: DiagnoseIssueInputSchema,
    outputSchema: DiagnoseIssueOutputSchema,
  },
  async input => {
    const {output} = await prompt(input);
    return output!;
  }
);
