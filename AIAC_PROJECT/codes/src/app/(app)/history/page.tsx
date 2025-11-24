import { serviceHistory } from '@/lib/data';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { format } from 'date-fns';

export default function HistoryPage() {
  return (
    <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold font-headline">Service History</h1>
        <p className="text-muted-foreground mt-2">A record of all your past services.</p>
      </div>

      <div className="space-y-4">
        {serviceHistory.map((service) => (
          <Card key={service.id}>
            <CardHeader>
              <div className="flex justify-between items-start">
                  <div>
                    <CardTitle className="text-lg">{service.service}</CardTitle>
                    <p className="text-sm text-muted-foreground">
                      Serviced by {service.mechanic} on {format(new Date(service.date), "MMMM d, yyyy")}
                    </p>
                  </div>
                  <Badge variant={service.status === 'Completed' ? 'default' : 'secondary'} className="bg-primary/80">
                      {service.status}
                  </Badge>
              </div>
            </CardHeader>
            <CardContent>
                <div className="flex justify-between items-center">
                    <p className="text-sm text-muted-foreground">Total Cost</p>
                    <p className="text-lg font-semibold">
                        ${service.cost.toFixed(2)}
                    </p>
                </div>
            </CardContent>
          </Card>
        ))}
        {serviceHistory.length === 0 && (
            <div className="text-center py-16 border-2 border-dashed rounded-lg">
                <p className="text-muted-foreground">No service history found.</p>
            </div>
        )}
      </div>
    </div>
  );
}
