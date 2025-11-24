import ChatInterface from '@/components/chat-interface';

export default function DiagnosePage() {
  return (
    <div className="container mx-auto max-w-3xl px-4 sm:px-6 lg:px-8 py-8">
      <div className="text-center mb-8">
        <h1 className="text-3xl font-bold font-headline">AI-Powered Diagnosis</h1>
        <p className="text-muted-foreground mt-2">Describe your car's issue to get an initial diagnosis.</p>
      </div>
      <ChatInterface />
    </div>
  );
}
