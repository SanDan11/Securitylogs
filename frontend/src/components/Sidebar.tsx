import { Link, useLocation } from "react-router-dom";

export default function Sidebar() {
  const location = useLocation();
  const links = [
    { path: "/", label: "Dashboard" },
    { path: "/users", label: "Users" },
    { path: "/incidents", label: "Incidents" },
    { path: "/dars", label: "Daily Reports" },
  ];

  return (
    <aside className="w-64 bg-gray-900 text-white flex flex-col p-6">
      <h1 className="text-xl font-bold mb-6 flex items-center gap-2">
        <span role="img" aria-label="shield">🛡️</span> Security Logs
      </h1>

      <nav className="space-y-2">
        {links.map((link) => (
          <Link
            key={link.path}
            to={link.path}
            className={`block px-3 py-2 rounded-md transition ${
              location.pathname === link.path
                ? "bg-blue-600"
                : "hover:bg-gray-700"
            }`}
          >
            {link.label}
          </Link>
        ))}
      </nav>
    </aside>
  );
}
