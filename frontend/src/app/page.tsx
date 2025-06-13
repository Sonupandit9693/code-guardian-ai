
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm">
        <h1 className="text-4xl font-bold text-center mb-8">
          AI Code Review Assistant
        </h1>
        <p className="text-xl text-center mb-4">
          Intelligent code review and analysis platform
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-8">
          <div className="p-6 border rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold mb-4">Code Quality</h2>
            <p>Automated analysis of code quality and best practices</p>
          </div>
          <div className="p-6 border rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold mb-4">Security</h2>
            <p>Comprehensive security vulnerability detection</p>
          </div>
          <div className="p-6 border rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold mb-4">Performance</h2>
            <p>Identify and optimize performance bottlenecks</p>
          </div>
        </div>
      </div>
    </main>
  );
}

// hey 
