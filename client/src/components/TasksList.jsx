// para crear un componente para que listar las tareas
import { useEffect, useState } from "react"; //para ralizazr peticiones al backend
import { getAllTasks } from "../api/tasks.api";
import { TaskCard } from "./TaskCard";

export function TasksList() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    async function loadTasks() {
      const res = await getAllTasks(); //peticion asincrona
      setTasks(res.data);
    }
    loadTasks();
  }, []);

  return (
    <div className="grid grid-cols-3 gap-3">
      {tasks.map((task) => (
        <TaskCard key={task.id} task = {task}/>
      ))}
    </div>
  );
}
