import Image from 'next/image';
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { Wrench, MapPin, CreditCard, Clock, Star, Bot } from 'lucide-react';
import placeholderImagesData from '@/lib/placeholder-images.json';

const heroImage = placeholderImagesData.placeholderImages.find(p => p.id === 'hero-car');

const features = [
  {
    icon: <Wrench className="h-8 w-8 text-primary" />,
    title: 'On-Road Emergency Assistance',
    description: 'Stuck with a flat tire or a dead battery? We’re on our way.',
  },
  {
    icon: <MapPin className="h-8 w-8 text-primary" />,
    title: 'Real-time Location Tracking',
    description: 'Watch your mechanic approach your location live on the map.',
  },
  {
    icon: <Star className="h-8 w-8 text-primary" />,
    title: 'Verified & Skilled Mechanics',
    description: 'All mechanics are vetted for skill, experience, and reliability.',
  },
  {
    icon: <CreditCard className="h-8 w-8 text-primary" />,
    title: 'Secure Online Payment',
    description: 'Pay securely through the app once your service is complete.',
  },
];

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen bg-background">
      <header className="container mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
        <div className="flex items-center gap-2">
           <Wrench className="h-8 w-8 text-primary" />
           <h1 className="text-2xl font-bold text-primary font-headline">Roadside Rescue</h1>
        </div>
        <Button asChild variant="ghost">
          <Link href="/dashboard">Enter App</Link>
        </Button>
      </header>

      <main className="flex-grow">
        {/* Hero Section */}
        <section className="relative text-center py-20 sm:py-32 lg:py-40 px-4 sm:px-6 lg:px-8 text-white overflow-hidden">
          {heroImage && (
            <Image
              src={heroImage.imageUrl}
              alt={heroImage.description}
              fill
              className="object-cover"
              data-ai-hint={heroImage.imageHint}
              priority
            />
          )}
          <div className="absolute inset-0 bg-primary/70"></div>
          <div className="relative container mx-auto">
            <h2 className="text-4xl sm:text-5xl lg:text-6xl font-extrabold font-headline">
              Stuck on the road? We’ve got your back.
            </h2>
            <p className="mt-4 max-w-2xl mx-auto text-lg sm:text-xl text-primary-foreground/90">
              Instant access to trusted mechanics when you need them most. Get help with a single tap.
            </p>
            <div className="mt-10">
              <Button asChild size="lg" className="bg-accent text-accent-foreground hover:bg-accent/90">
                <Link href="/dashboard">Get Help Now</Link>
              </Button>
            </div>
          </div>
        </section>
        
        {/* How It Works Section */}
        <section className="py-16 sm:py-24 bg-card">
          <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center">
              <h3 className="text-3xl sm:text-4xl font-bold text-foreground font-headline">
                How It Works
              </h3>
              <p className="mt-3 max-w-2xl mx-auto text-lg text-muted-foreground">
                Get back on the road in 3 simple steps.
              </p>
            </div>
            <div className="mt-12 grid gap-8 md:grid-cols-3">
              <div className="text-center">
                 <div className="flex items-center justify-center h-16 w-16 rounded-full bg-accent/20 text-accent mx-auto">
                   <MapPin className="h-8 w-8" />
                 </div>
                 <h4 className="mt-5 text-lg font-medium text-foreground">1. Pinpoint Your Location</h4>
                 <p className="mt-2 text-base text-muted-foreground">
                   Use our app to share your location instantly.
                 </p>
              </div>
              <div className="text-center">
                 <div className="flex items-center justify-center h-16 w-16 rounded-full bg-accent/20 text-accent mx-auto">
                   <Wrench className="h-8 w-8" />
                 </div>
                 <h4 className="mt-5 text-lg font-medium text-foreground">2. Book a Mechanic</h4>
                 <p className="mt-2 text-base text-muted-foreground">
                   Choose from available nearby mechanics and book instantly.
                 </p>
              </div>
              <div className="text-center">
                 <div className="flex items-center justify-center h-16 w-16 rounded-full bg-accent/20 text-accent mx-auto">
                   <Clock className="h-8 w-8" />
                 </div>
                 <h4 className="mt-5 text-lg font-medium text-foreground">3. Get Back to Your Journey</h4>
                 <p className="mt-2 text-base text-muted-foreground">
                   Your mechanic arrives, fixes the issue, and you're on your way.
                 </p>
              </div>
            </div>
          </div>
        </section>

        {/* Features Section */}
        <section className="py-16 sm:py-24">
          <div className="container mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center">
              <h3 className="text-3xl sm:text-4xl font-bold text-foreground font-headline">
                Travel Without Worry
              </h3>
              <p className="mt-3 max-w-2xl mx-auto text-lg text-muted-foreground">
                Everything you need for a stress-free journey.
              </p>
            </div>
            <div className="mt-16 grid gap-10 sm:grid-cols-2 lg:grid-cols-4">
              {features.map((feature) => (
                <div key={feature.title} className="text-center">
                  {feature.icon}
                  <h4 className="mt-5 text-lg font-medium text-foreground">{feature.title}</h4>
                  <p className="mt-2 text-base text-muted-foreground">{feature.description}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* AI Diagnosis Section */}
        <section className="bg-primary text-primary-foreground py-16 sm:py-24">
          <div className="container mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <Bot className="h-12 w-12 mx-auto text-accent" />
            <h3 className="mt-4 text-3xl sm:text-4xl font-bold font-headline">Not Sure What's Wrong?</h3>
            <p className="mt-3 max-w-2xl mx-auto text-lg text-primary-foreground/80">
              Use our AI-powered tool to diagnose the issue before you even book a mechanic.
            </p>
            <div className="mt-8">
              <Button asChild variant="outline" size="lg" className="border-accent text-accent hover:bg-accent hover:text-accent-foreground">
                <Link href="/diagnose">Try AI Diagnosis</Link>
              </Button>
            </div>
          </div>
        </section>
      </main>

      <footer className="bg-card py-8">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 text-center text-muted-foreground">
          <p>&copy; {new Date().getFullYear()} Roadside Rescue. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}
