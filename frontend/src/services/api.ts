const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface CodeReviewRequest {
  repository: string;
  pullRequest: number;
  branch?: string;
}

export interface CodeReviewResponse {
  id: string;
  status: 'pending' | 'completed' | 'failed';
  findings: {
    type: 'quality' | 'security' | 'performance';
    severity: 'low' | 'medium' | 'high';
    message: string;
    location: string;
    suggestion?: string;
  }[];
}

export const api = {
  async submitCodeReview(data: CodeReviewRequest): Promise<CodeReviewResponse> {
    const response = await fetch(`${API_URL}/api/reviews`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error('Failed to submit code review');
    }

    return response.json();
  },

  async getCodeReview(id: string): Promise<CodeReviewResponse> {
    const response = await fetch(`${API_URL}/api/reviews/${id}`);

    if (!response.ok) {
      throw new Error('Failed to fetch code review');
    }

    return response.json();
  },
}; 