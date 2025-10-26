export default function App() {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-50">
      <h1 className="text-4xl font-bold text-blue-600 mb-4">
        🛡️ Security Logs Dashboard
      </h1>
      <p className="text-gray-700 text-lg">
        Tailwind CSS is working correctly!
      </p>

      <div className="mt-8 p-4 bg-white rounded-2xl shadow-md w-80 text-center">
        <h2 className="text-xl font-semibold mb-2">Latest Alert</h2>
        <p className="text-red-600 font-medium">Unauthorized access detected 🚨</p>
      </div>
    </div>
  );
}
