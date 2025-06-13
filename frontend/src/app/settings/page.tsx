export default function SettingsPage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="z-10 max-w-5xl w-full">
        <h1 className="text-4xl font-bold text-center mb-8">
          Settings
        </h1>
        <p className="text-xl text-center mb-4">
          Configure your AI Code Review Assistant
        </p>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">
          <div className="p-6 border rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold mb-4">GitHub Integration</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium mb-2">GitHub Token</label>
                <input 
                  type="password" 
                  className="w-full p-2 border rounded" 
                  placeholder="Enter your GitHub token"
                />
              </div>
              <button className="w-full p-2 bg-blue-500 text-white rounded hover:bg-blue-600">
                Connect GitHub
              </button>
            </div>
          </div>
          <div className="p-6 border rounded-lg shadow-lg">
            <h2 className="text-2xl font-semibold mb-4">AI Configuration</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium mb-2">OpenAI API Key</label>
                <input 
                  type="password" 
                  className="w-full p-2 border rounded" 
                  placeholder="Enter your OpenAI API key"
                />
              </div>
              <div>
                <label className="block text-sm font-medium mb-2">Review Sensitivity</label>
                <select className="w-full p-2 border rounded">
                  <option>High</option>
                  <option>Medium</option>
                  <option>Low</option>
                </select>
              </div>
              <button className="w-full p-2 bg-green-500 text-white rounded hover:bg-green-600">
                Save Configuration
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}

