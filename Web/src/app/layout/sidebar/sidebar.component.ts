import { CommonModule } from '@angular/common';
import { Component, inject, signal } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';

import { AuthService } from '../../core/services/auth.service';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [CommonModule, RouterLink, RouterLinkActive],
  templateUrl: './sidebar.component.html',
})
export class SidebarComponent {
  readonly auth = inject(AuthService);
  readonly profileOpen = signal(false);

  readonly navItems = [
    { label: 'Dashboard', path: '/dashboard', icon: 'home' },
    { label: 'My Notebooks', path: '/dashboard', icon: 'book' },
    { label: 'AI Tutor', path: '/dashboard', icon: 'bot' },
    { label: 'Mock Tests', path: '/dashboard', icon: 'quiz' },
    { label: 'Study Path', path: '/dashboard', icon: 'path' },
    { label: 'Analytics', path: '/dashboard', icon: 'chart' },
    { label: 'Settings', path: '/dashboard', icon: 'settings' },
  ];

  toggleProfile(): void {
    this.profileOpen.update((open) => !open);
  }

  signOut(): void {
    this.profileOpen.set(false);
    this.auth.logout().subscribe();
  }
}
