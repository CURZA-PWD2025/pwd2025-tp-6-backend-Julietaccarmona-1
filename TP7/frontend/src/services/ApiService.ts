import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export const ApiService = {
  // GET /lista
  async getAll<T>(url: string): Promise<T> {
    const { data } = await api.get<T>(url);
    return data;
  },

  // GET /1
  async getOne<T>(url: string): Promise<T> {
    const { data } = await api.get<T>(url);
    return data;
  },

  // POST
  async post<T>(url: string, payload: object): Promise<T> {
    const { data } = await api.post<T>(url, payload);
    return data;
  },

  // PUT
  async put<T>(url: string, payload: object): Promise<T> {
    const { data } = await api.put<T>(url, payload);
    return data;
  },

  // DELETE
  async del<T>(url: string): Promise<T> {
    const { data } = await api.delete<T>(url);
    return data;
  },
};
