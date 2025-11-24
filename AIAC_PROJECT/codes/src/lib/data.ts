export type Mechanic = {
  id: string;
  name: string;
  specialty: string;
  rating: number;
  reviews: number;
  eta: number; // in minutes
  avatarUrl: string;
  location: { lat: number; lng: number };
};

export const mechanics: Mechanic[] = [
  {
    id: '1',
    name: 'John "Sparky" Doe',
    specialty: 'Engine & Electrical',
    rating: 4.9,
    reviews: 124,
    eta: 8,
    avatarUrl: 'https://picsum.photos/seed/mech1/100/100',
    location: { lat: 34.0522, lng: -118.2437 },
  },
  {
    id: '2',
    name: 'Maria Garcia',
    specialty: 'Tires & Brakes',
    rating: 4.8,
    reviews: 89,
    eta: 12,
    avatarUrl: 'https://picsum.photos/seed/mech2/100/100',
    location: { lat: 34.055, lng: -118.25 },
  },
  {
    id: '3',
    name: 'Sam Wilson',
    specialty: 'General Maintenance',
    rating: 4.7,
    reviews: 210,
    eta: 15,
    avatarUrl: 'https://picsum.photos/seed/mech3/100/100',
    location: { lat: 34.04, lng: -118.24 },
  },
];

export type Service = {
  id: string;
  date: string;
  service: string;
  mechanic: string;
  cost: number;
  status: 'Completed' | 'In Progress' | 'Cancelled';
};

export const serviceHistory: Service[] = [
  {
    id: 's1',
    date: '2024-07-15',
    service: 'Flat Tire Replacement',
    mechanic: 'Maria Garcia',
    cost: 85.0,
    status: 'Completed',
  },
  {
    id: 's2',
    date: '2024-05-20',
    service: 'Battery Jump-Start',
    mechanic: 'John "Sparky" Doe',
    cost: 50.0,
    status: 'Completed',
  },
  {
    id: 's3',
    date: '2024-02-10',
    service: 'Engine Diagnostic',
    mechanic: 'Sam Wilson',
    cost: 120.0,
    status: 'Completed',
  },
];
