import React from 'react';
import MobileNav from '@/components/layout/mobile-nav';
import AppHeader from '@/components/layout/app-header';

export default function AppLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex flex-col h-full">
      <AppHeader />
      <main className="flex-grow overflow-y-auto pb-20 md:pb-0">
        {children}
      </main>
      <MobileNav />
    </div>
  );
}
