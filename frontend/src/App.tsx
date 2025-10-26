import { Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Dashboard from "./pages/Dashboard";
import Users from "./pages/Users";
import Incidents from "./pages/Incidents";
import DARs from "./pages/DARs";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Dashboard />} />
        <Route path="users" element={<Users />} />
        <Route path="incidents" element={<Incidents />} />
        <Route path="dars" element={<DARs />} />
      </Route>
    </Routes>
  );
}
