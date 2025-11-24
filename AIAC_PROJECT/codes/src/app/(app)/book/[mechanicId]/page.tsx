'use client'
import { useParams, useRouter } from 'next/navigation';
import { mechanics } from '@/lib/data';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
import { Button } from '@/components/ui/button';
import { ArrowLeft, Clock, Star, ShieldCheck } from 'lucide-react';
import { useToast } from "@/hooks/use-toast"
import { useState } from 'react';

export default function BookingPage() {
    const params = useParams();
    const router = useRouter();
    const { toast } = useToast();
    const [isBooking, setIsBooking] = useState(false);

    const mechanic = mechanics.find(m => m.id === params.mechanicId);

    if (!mechanic) {
        return (
            <div className="container mx-auto text-center py-20">
                <p>Mechanic not found.</p>
                <Button onClick={() => router.back()} className="mt-4">Go Back</Button>
            </div>
        );
    }
    
    const handleBooking = () => {
        setIsBooking(true);
        // Simulate API call
        setTimeout(() => {
            toast({
                title: "Booking Confirmed!",
                description: `${mechanic.name} is on their way.`,
            });
            // Redirect to dashboard, in a real app this would go to a tracking page
            router.push('/dashboard');
            setIsBooking(false);
        }, 1500);
    };

    return (
        <div className="container mx-auto max-w-2xl px-4 sm:px-6 lg:px-8 py-8">
            <Button variant="ghost" onClick={() => router.back()} className="mb-4">
                <ArrowLeft className="mr-2 h-4 w-4" />
                Back to list
            </Button>
            <Card>
                <CardHeader>
                    <CardTitle className="text-2xl">Confirm Your Booking</CardTitle>
                    <CardDescription>You are booking {mechanic.name} for immediate assistance.</CardDescription>
                </CardHeader>
                <CardContent className="space-y-6">
                    <div className="flex items-center gap-4 p-4 border rounded-lg">
                        <Avatar className="h-20 w-20">
                            <AvatarImage src={mechanic.avatarUrl} alt={mechanic.name} />
                            <AvatarFallback>{mechanic.name.charAt(0)}</AvatarFallback>
                        </Avatar>
                        <div className="flex-1">
                            <h3 className="text-xl font-bold">{mechanic.name}</h3>
                            <p className="text-muted-foreground">{mechanic.specialty}</p>
                            <div className="flex items-center gap-4 mt-2 text-sm">
                                <div className="flex items-center gap-1">
                                    <Star className="w-4 h-4 text-accent fill-accent" />
                                    <span className="font-semibold">{mechanic.rating}</span>
                                </div>
                                <div className="flex items-center gap-1">
                                    <Clock className="w-4 h-4 text-muted-foreground" />
                                    <span>{mechanic.eta} min ETA</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="p-4 bg-secondary/50 rounded-lg">
                        <h4 className="font-semibold mb-2">Service Details</h4>
                        <div className="text-sm space-y-2 text-muted-foreground">
                            <p><span className="font-medium text-foreground">Service Type:</span> Emergency Roadside Assistance</p>
                            <p><span className="font-medium text-foreground">Your Location:</span> Current Location (approx.)</p>
                            <p className="italic">Note: A base service fee applies. Additional costs for parts and labor will be determined on-site.</p>
                        </div>
                    </div>
                </CardContent>
                <CardFooter>
                    <Button 
                        className="w-full bg-accent text-accent-foreground hover:bg-accent/90" 
                        size="lg"
                        onClick={handleBooking}
                        disabled={isBooking}
                    >
                        {isBooking ? "Confirming..." : `Confirm & Book ${mechanic.name}`}
                    </Button>
                </CardFooter>
            </Card>
        </div>
    );
}
