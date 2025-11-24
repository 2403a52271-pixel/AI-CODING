'use client';

import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';
import { Bot, User, Send, CircleDashed, ClipboardCheck } from 'lucide-react';

import { diagnoseIssue, type DiagnoseIssueInput } from '@/ai/flows/ai-diagnose-issue';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Form, FormControl, FormField, FormItem } from '@/components/ui/form';
import { Avatar, AvatarFallback } from '@/components/ui/avatar';
import { useToast } from '@/hooks/use-toast';
import { ScrollArea } from '@/components/ui/scroll-area';

type Message = {
  role: 'user' | 'assistant';
  content: string;
};

const formSchema = z.object({
  message: z.string().min(1, 'Message cannot be empty'),
});

export default function ChatInterface() {
  const [conversation, setConversation] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [diagnosisResult, setDiagnosisResult] = useState<{ diagnosis: string; relevantDataPoints: string[] } | null>(null);
  const { toast } = useToast();

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      message: '',
    },
  });

  async function onSubmit(values: z.infer<typeof formSchema>) {
    const userMessage: Message = { role: 'user', content: values.message };
    const newConversation = [...conversation, userMessage];
    setConversation(newConversation);
    form.reset();
    setIsLoading(true);
    setDiagnosisResult(null);

    try {
        const input: DiagnoseIssueInput = {
            issueDescription: values.message,
            conversationHistory: conversation
        }
        const result = await diagnoseIssue(input);

        if (result.diagnosis) {
            setDiagnosisResult(result);
            const assistantMessage: Message = { role: 'assistant', content: result.diagnosis };
            setConversation(prev => [...prev, assistantMessage]);
        } else {
             toast({
                variant: "destructive",
                title: "Diagnosis Error",
                description: "The AI could not provide a diagnosis. Please try rephrasing your issue.",
            });
        }
    } catch (error) {
        console.error('AI diagnosis error:', error);
        toast({
            variant: "destructive",
            title: "An Error Occurred",
            description: "Failed to communicate with the AI service. Please try again later.",
        });
    } finally {
        setIsLoading(false);
    }
  }

  return (
    <Card className="flex flex-col h-[70vh]">
      <CardHeader>
        <CardTitle>Chat with our AI Mechanic</CardTitle>
      </CardHeader>
      <ScrollArea className="flex-grow p-4">
        <div className="space-y-4">
          {conversation.map((msg, index) => (
            <div key={index} className={`flex items-start gap-3 ${msg.role === 'user' ? 'justify-end' : ''}`}>
              {msg.role === 'assistant' && (
                <Avatar className="w-8 h-8">
                  <AvatarFallback className="bg-primary text-primary-foreground"><Bot className="w-5 h-5" /></AvatarFallback>
                </Avatar>
              )}
              <div className={`rounded-lg px-4 py-2 max-w-[80%] ${msg.role === 'user' ? 'bg-primary text-primary-foreground' : 'bg-secondary'}`}>
                <p className="text-sm">{msg.content}</p>
              </div>
              {msg.role === 'user' && (
                <Avatar className="w-8 h-8">
                  <AvatarFallback><User className="w-5 h-5" /></AvatarFallback>
                </Avatar>
              )}
            </div>
          ))}
          {isLoading && (
            <div className="flex items-start gap-3">
              <Avatar className="w-8 h-8">
                 <AvatarFallback className="bg-primary text-primary-foreground"><Bot className="w-5 h-5" /></AvatarFallback>
              </Avatar>
              <div className="rounded-lg px-4 py-2 bg-secondary flex items-center gap-2">
                 <CircleDashed className="animate-spin h-4 w-4" />
                 <p className="text-sm text-muted-foreground">AI is thinking...</p>
              </div>
            </div>
          )}
        </div>
      </ScrollArea>
      {diagnosisResult && (
        <CardContent className="border-t p-4 bg-accent/10">
            <h4 className="font-semibold flex items-center gap-2"><ClipboardCheck className="w-5 h-5 text-accent"/> AI Diagnosis Summary</h4>
            <p className="text-sm mt-2">{diagnosisResult.diagnosis}</p>
            <h5 className="font-semibold mt-4 text-sm">Data points to record:</h5>
            <ul className="list-disc list-inside text-sm text-muted-foreground mt-1 space-y-1">
                {diagnosisResult.relevantDataPoints.map((point, i) => <li key={i}>{point}</li>)}
            </ul>
        </CardContent>
      )}
      <CardFooter className="p-4 border-t">
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)} className="flex w-full items-center space-x-2">
            <FormField
              control={form.control}
              name="message"
              render={({ field }) => (
                <FormItem className="flex-1">
                  <FormControl>
                    <Input placeholder="e.g., 'My car is making a clicking sound...'" {...field} disabled={isLoading} />
                  </FormControl>
                </FormItem>
              )}
            />
            <Button type="submit" size="icon" disabled={isLoading}>
              <Send className="h-4 w-4" />
            </Button>
          </form>
        </Form>
      </CardFooter>
    </Card>
  );
}
