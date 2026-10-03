import { useEffect, useState } from "react";
import api from "../services/api";
import { FaRobot } from "react-icons/fa";

function Dashboard() {
  const [leads, setLeads] = useState([]);

  useEffect(() => {
    api.get("/leads")
      .then((res) => setLeads(res.data))
      .catch(console.error);
  }, []);

  const highPriority = leads.filter(
    (lead) => lead.priority === "High"
  ).length;

  const avgScore =
    leads.length > 0
      ? Math.round(
          leads.reduce((sum, lead) => sum + lead.score, 0) / leads.length
        )
      : 0;

  return (
    <div className="min-h-screen bg-slate-100 p-8">

      <div className="flex items-center gap-4 mb-8">
        <FaRobot className="text-5xl text-blue-600" />
        <h1 className="text-5xl font-bold">
          LeadPilot AI Dashboard
        </h1>
      </div>

      <div className="grid grid-cols-3 gap-6 mb-10">

        <div className="bg-white rounded-xl shadow p-6">
          <h3 className="text-gray-500">Total Leads</h3>
          <h1 className="text-4xl font-bold">
            {leads.length}
          </h1>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <h3 className="text-gray-500">High Priority</h3>
          <h1 className="text-4xl font-bold text-red-500">
            {highPriority}
          </h1>
        </div>

        <div className="bg-white rounded-xl shadow p-6">
          <h3 className="text-gray-500">Average AI Score</h3>
          <h1 className="text-4xl font-bold text-green-600">
            {avgScore}
          </h1>
        </div>

      </div>

      <div className="bg-white rounded-xl shadow p-6">

        <h2 className="text-2xl font-bold mb-5">
          All Leads
        </h2>

        <table className="w-full">

          <thead>

            <tr className="border-b">

              <th className="text-left p-3">Company</th>

              <th className="text-left p-3">Contact</th>

              <th className="text-left p-3">Score</th>

              <th className="text-left p-3">Priority</th>

              <th className="text-left p-3">Assigned To</th>

              <th className="text-left p-3">Status</th>

            </tr>

          </thead>

          <tbody>

            {leads.map((lead) => (

              <tr key={lead.id} className="border-b">

                <td className="p-3">{lead.company}</td>

                <td className="p-3">{lead.contact_name}</td>

                <td className="p-3 font-bold">
                  {lead.score}
                </td>

                <td className="p-3">

                  <span
                    className={`px-3 py-1 rounded-full text-white ${
                      lead.priority === "High"
                        ? "bg-red-500"
                        : lead.priority === "Medium"
                        ? "bg-yellow-500"
                        : "bg-green-500"
                    }`}
                  >
                    {lead.priority}
                  </span>

                </td>

                <td className="p-3">
                  {lead.assigned_to}
                </td>

                <td className="p-3">
                  {lead.status}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default Dashboard;