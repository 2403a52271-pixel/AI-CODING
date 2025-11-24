import Link from 'next/link';
import { Wrench, User } from 'lucide-react';
import { Button } from '@/components/ui/button';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export default function AppHeader() {
  return (
    <header className="sticky top-0 z-40 w-full border-b bg-card">
      <div className="container flex h-16 items-center px-4 sm:px-6 lg:px-8">
        <Link href="/dashboard" className="flex items-center gap-2 mr-auto">
          <Wrench className="h-7 w-7 text-primary" />
          <span className="font-bold text-lg text-primary hidden sm:inline-block">
            Roadside Rescue
          </span>
        </Link>
        
        <nav className="hidden md:flex items-center space-x-2">
           <Button variant="ghost" asChild>
              <Link href="/dashboard">Find Mechanic</Link>
           </Button>
           <Button variant="ghost" asChild>
              <Link href="/diagnose">AI Diagnosis</Link>
           </Button>
           <Button variant="ghost" asChild>
              <Link href="/history">Service History</Link>
           </Button>
        </nav>

        <div className="ml-4">
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="ghost" className="relative h-8 w-8 rounded-full">
                <User className="h-5 w-5" />
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent className="w-56" align="end" forceMount>
              <DropdownMenuLabel className="font-normal">
                <div className="flex flex-col space-y-1">
                  <p className="text-sm font-medium leading-none">User</p>
                  <p className="text-xs leading-none text-muted-foreground">
                    user@example.com
                  </p>
                </div>
              </DropdownMenuLabel>
              <DropdownMenuSeparator />
              <DropdownMenuItem>Profile</DropdownMenuItem>
              <DropdownMenuItem>Settings</DropdownMenuItem>
              <DropdownMenuSeparator />
              <DropdownMenuItem>Log out</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>
    </header>
  );
}
