import { CommonModule } from '@angular/common';
import { Component, computed, inject } from '@angular/core';

import { AuthService } from '../../../../core/services/auth.service';

@Component({
  selector: 'app-dashboard-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard-home.component.html',
})
export class DashboardHomeComponent {
  private readonly auth = inject(AuthService);

  readonly greetingName = computed(() => {
    const name = this.auth.user()?.name?.trim() || 'there';
    const first = name.split(/\s+/)[0];
    return first;
  });

  readonly goalProgress = 65;

  readonly stats = [
    { label: 'Study Streak', value: '7 Days', hint: 'Keep it going' },
    { label: 'This Week', value: '12.5 hrs', hint: 'Focused study' },
    { label: 'Quiz Average', value: '88%', hint: 'Last 5 quizzes' },
  ];

  readonly notebooks = [
    { title: 'AI Fundamentals', edited: 'Last edited 2h ago' },
    { title: 'Vector Databases', edited: 'Last edited yesterday' },
    { title: 'Python for ML', edited: 'Last edited 3 days ago' },
  ];
}
