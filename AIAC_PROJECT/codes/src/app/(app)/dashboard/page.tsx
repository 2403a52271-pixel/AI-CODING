import Image from 'next/image';
import { mechanics } from '@/lib/data';
import placeholderImages from '@/lib/placeholder-images.json';
import MechanicCard from '@/components/mechanic-card';
import { Card } from '@/components/ui/card';
import { Wrench } from 'lucide-react';

const mapImage = placeholderImages.placeholderImages.find(p => p.id === 'map-background');

export default function DashboardPage() {
  return (
    <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="text-center mb-8">
        <h1 className="text-3xl font-bold font-headline">Find a Mechanic Nearby</h1>
        <p className="text-muted-foreground mt-2">Available mechanics are shown below. Select one to proceed.</p>
      </div>

      <Card className="overflow-hidden shadow-lg">
        <div className="relative h-64 md:h-[450px] w-full">
          {mapImage && (
             <Image
              src={mapImage.imageUrl}
              alt={mapImage.description}
              fill
              className="object-cover"
              data-ai-hint={mapImage.imageHint}
            />
          )}
          <div className="absolute inset-0 bg-black/10 flex items-center justify-center">
            {/* User location pin */}
            <div className="relative">
              <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 h-8 w-8 rounded-full bg-accent opacity-50 animate-ping"></div>
              <div className="relative h-4 w-4 rounded-full bg-accent border-2 border-white shadow-md"></div>
            </div>

            {/* Mock mechanic pins */}
            <div className="absolute top-[30%] left-[25%]">
                <Wrench className="h-8 w-8 text-primary drop-shadow-lg" />
            </div>
            <div className="absolute top-[60%] left-[70%]">
                <Wrench className="h-8 w-8 text-primary drop-shadow-lg" />
            </div>
             <div className="absolute top-[50%] left-[40%]">
                <Wrench className="h-8 w-8 text-primary drop-shadow-lg" />
            </div>
          </div>
        </div>
      </Card>
      
      <div className="mt-8">
        <h2 className="text-2xl font-bold mb-4">Available Now</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {mechanics.map((mechanic) => (
            <MechanicCard key={mechanic.id} mechanic={mechanic} />
          ))}
        </div>
      </div>
    </div>
  );
}
