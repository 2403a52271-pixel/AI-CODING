import Image from 'next/image';
import Link from 'next/link';
import type { Mechanic } from '@/lib/data';
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
import { Button } from '@/components/ui/button';
import { Star, Clock } from 'lucide-react';

type MechanicCardProps = {
  mechanic: Mechanic;
};

export default function MechanicCard({ mechanic }: MechanicCardProps) {
  return (
    <Card className="flex flex-col transition-all hover:shadow-md">
      <CardHeader className="flex flex-row items-center gap-4">
        <Avatar className="h-16 w-16">
          <AvatarImage src={mechanic.avatarUrl} alt={mechanic.name} />
          <AvatarFallback>{mechanic.name.charAt(0)}</AvatarFallback>
        </Avatar>
        <div className="flex-1">
          <CardTitle className="text-xl">{mechanic.name}</CardTitle>
          <p className="text-sm text-muted-foreground">{mechanic.specialty}</p>
        </div>
      </CardHeader>
      <CardContent className="flex-grow">
        <div className="flex justify-between items-center text-sm">
          <div className="flex items-center gap-1">
            <Star className="w-4 h-4 text-accent fill-accent" />
            <span className="font-semibold">{mechanic.rating}</span>
            <span className="text-muted-foreground">({mechanic.reviews} reviews)</span>
          </div>
          <div className="flex items-center gap-1">
            <Clock className="w-4 h-4 text-muted-foreground" />
            <span>{mechanic.eta} min ETA</span>
          </div>
        </div>
      </CardContent>
      <CardFooter>
        <Button asChild className="w-full bg-accent text-accent-foreground hover:bg-accent/90">
          <Link href={`/book/${mechanic.id}`}>Book Now</Link>
        </Button>
      </CardFooter>
    </Card>
  );
}
