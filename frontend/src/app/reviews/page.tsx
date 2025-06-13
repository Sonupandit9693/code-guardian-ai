export default function ReviewsPage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="z-10 max-w-5xl w-full">
        <h1 className="text-4xl font-bold text-center mb-8">
          Code Reviews
        </h1>
        <p className="text-xl text-center mb-4">
          AI-powered code review history and management
        </p>
        <div className="grid grid-cols-1 gap-6 mt-8">
          <div className="p-6 border rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold mb-4">Review History</h2>
            <p className="text-gray-600">No reviews yet. Connect your GitHub repository to get started.</p>
          </div>
          <div className="p-6 border rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold mb-4">Pending Reviews</h2>
            <p className="text-gray-600">No pending reviews</p>
          </div>
          <div className="p-6 border rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold mb-4">Quick Actions</h2>
            <div className="space-y-2">
              <button className="w-full p-2 bg-blue-500 text-white rounded hover:bg-blue-600">
                Analyze Current Repository
              </button>
              <button className="w-full p-2 bg-green-500 text-white rounded hover:bg-green-600">
                Start New Review
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}

