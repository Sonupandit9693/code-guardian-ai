export default function DashboardPage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="z-10 max-w-5xl w-full">
        <h1 className="text-4xl font-bold text-center mb-8">
          Dashboard
        </h1>
        <p className="text-xl text-center mb-4">
          Your AI Code Review Dashboard
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-8">
          <div className="p-6 border rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold mb-4">Recent Reviews</h2>
            <p className="text-gray-600">No recent reviews</p>
          </div>
          <div className="p-6 border rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold mb-4">Active Projects</h2>
            <p className="text-gray-600">Connect your GitHub repositories</p>
          </div>
          <div className="p-6 border rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold mb-4">Code Quality</h2>
            <p className="text-gray-600">Overall score will appear here</p>
          </div>
        </div>
      </div>
    </main>
  );
}

