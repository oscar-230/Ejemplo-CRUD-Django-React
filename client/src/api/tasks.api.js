import axios from 'axios' //axios para hacer peticiones al backend


const taskApi = axios.create({
    baseURL: 'http://localhost:8000/task/api/v1/task/'
})
// para hacer peticiones al backend -> traer la lista de tareas
export const getAllTasks = () => taskApi.get('/');

export const getTask = (id) => taskApi.get('/' + id +'/');

export const createTask = (task)=> taskApi.post('/', task);

export const deleteTask = (id)=> taskApi.delete(`/${id}`);

export const updateTask = (id, task)=> taskApi.put(`/${id}/`, task); 