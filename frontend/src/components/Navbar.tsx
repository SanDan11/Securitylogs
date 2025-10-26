export default function Navbar() {
  return (
    <header className="flex justify-between items-center bg-white shadow px-6 py-3">
      <h2 className="text-xl font-semibold text-gray-800">Security Logs Admin Panel</h2>
      <div className="flex items-center space-x-4">
        <span className="text-gray-600 text-sm">Admin</span>
        <div className="w-8 h-8 bg-gray-300 rounded-full"></div>
      </div>
    </header>
  );
}
