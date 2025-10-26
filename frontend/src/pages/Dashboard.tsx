import { useEffect, useState } from "react";
import { fetchUsers } from "../services/testApi";

export default function Dashboard() {
  const [users, setUsers] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchUsers()
      .then((data) => setUsers(data))
      .catch((err) => setError("Failed to load users"))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p className="text-gray-500">Loading users...</p>;
  if (error) return <p className="text-red-500">{error}</p>;

  return (
    <div>
      <h1 className="text-3xl font-bold text-blue-600 mb-4">Dashboard</h1>
      <ul className="space-y-2">
        {users.map((user) => (
          <li key={user.id} className="bg-white p-3 rounded shadow">
            <strong>{user.name || "Unnamed User"}</strong> — {user.role}
          </li>
        ))}
      </ul>
    </div>
  );
}
