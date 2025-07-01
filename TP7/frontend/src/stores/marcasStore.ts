import { defineStore } from "pinia";
import { ApiService } from "@/services/ApiService";
import type { Marca } from "@/types/Marca";


export const useMarcasStore = defineStore("marcas", {
    state: () => ({
     lista: [] as Marca[],
     actual: null as Marca | null,
     loading: false,
    }),
  actions: {
    async fetchAll() {
      this.loading = true;
      this.lista = await ApiService.getAll("/marcas/");
      this.loading = false;
    },
    async create(data:any) {
      await ApiService.post("/marcas/", data);
      await this.fetchAll();
    },
    async update(id:number,data:any) {
      await ApiService.put(`/marcas/${id}`, data);
      await this.fetchAll();
    },
    async remove(id:number) {
      await ApiService.del(`/marcas/${id}`);
      await this.fetchAll();
    },
    async fetchOne(id: number) {
     this.actual = await ApiService.getOne<Marca>(`/marcas/${id}`);
    },
  },
});
