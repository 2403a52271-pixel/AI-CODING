'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Map, Bot, History } from 'lucide-react';
import { cn } from '@/lib/utils';

const navItems = [
  { href: '/dashboard', label: 'Find', icon: Map },
  { href: '/diagnose', label: 'Diagnose', icon: Bot },
  { href: '/history', label: 'History', icon: History },
];

export default function MobileNav() {
  const pathname = usePathname();

  return (
    <div className="md:hidden fixed bottom-0 left-0 right-0 h-16 bg-card border-t z-50">
      <nav className="h-full">
        <ul className="h-full flex justify-around items-center">
          {navItems.map((item) => {
            const isActive = pathname.startsWith(item.href);
            return (
              <li key={item.href}>
                <Link href={item.href} className="flex flex-col items-center gap-1">
                  <item.icon
                    className={cn(
                      'h-6 w-6',
                      isActive ? 'text-primary' : 'text-muted-foreground'
                    )}
                  />
                  <span
                    className={cn(
                      'text-xs',
                      isActive ? 'text-primary font-semibold' : 'text-muted-foreground'
                    )}
                  >
                    {item.label}
                  </span>
                </Link>
              </li>
            );
          })}
        </ul>
      </nav>
    </div>
  );
}
