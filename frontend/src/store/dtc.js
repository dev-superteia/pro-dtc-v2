import { defineStore } from "pinia";
import axios from "axios";
export const useDtcStore = defineStore({
  id: "dtc",
  state: () => ({
    plant: [],
    mkg: [],
    line: [],
    type: [],
    typeListMat: [],
    typeListRaw: [],
    tissue: [],
  }),
  actions: {
    async setPlant() {
      if (this.plant.length > 0) {
        return this.plant;
      } else {
        const response = await axios.get(
          "http://localhost:8000/api/v1/multselect/plant"
        );
        this.plant.push({ text: "All", value: "" });
        for (let i = 0; i < response.data.length; i++) {
          this.plant.push({
            text: response.data[i].plant + " - " + response.data[i].plant_desc,
            value: response.data[i].plant,
          });
        }
        return this.plant;
      }
    },
    async setMkg() {
      if (this.mkg.length == 0) {
        const response = await axios.get(
          "http://localhost:8000/api/v1/multselect/market_segment"
        );
        this.mkg.push({ text: "All", value: "" });
        for (let i = 0; i < response.data.length; i++) {
          const nome = response.data[i].denomination
            ? " - " + response.data[i].denomination
            : "";
          this.mkg.push({
            text: response.data[i].mkg_segm + nome,
            value: response.data[i].mkg_segm,
          });
        }
      }
    },
    async setLine() {
      if (this.line.length == 0) {
        const response = await axios.get(
          "http://localhost:8000/api/v1/multselect/line"
        );
        this.line.push({ text: "All", value: "" });
        for (let i = 0; i < response.data.length; i++) {
          this.line.push({
            text: response.data[i].line,
            value: response.data[i].line,
          });
        }
      }
    },
    async setType() {
      if (this.plant.length == 0) {
        this.type.push({ text: "Material", value: "material" });
        this.type.push({ text: "Raw Material", value: "raw" });
      }
    },
    async setTypeListMat() {
      const response = await axios.get(
        "http://localhost:8000/api/v1/multselect/mass"
      );

      for (let i = 0; i < response.data.length; i++) {
        this.typeListMat.push({
          text: response.data[i].material,
          value: response.data[i].material,
        });
      }
    },
    async setTypeListRaw() {
      const response = await axios.get(
        "http://localhost:8000/api/v1/multselect/raw_material"
      );
      for (let i = 0; i < response.data.length; i++) {
        this.typeListRaw.push({
          text: response.data[i].material,
          value: response.data[i].material,
        });
      }
    },
    async setTissue(plant, year) {
        console.log(plant.value,year);
      if (this.tissue.length > 0) {
        return this.tissue;
      } else {
        const response = await axios.get("http://localhost:8000/api/v1/tissue/?plant="+plant.value+"&year="+year);
        this.tissue = response.data;
        this.tissue.forEach((element, index) => {
          var array = [];
          for (let index = 0; index < 13; index++) {
            var searchFind = element.array_agg.find((el) => {
              return el[0] == index || (el[0] == "std" && index == 0);
            });
            if (searchFind) {
              array.push(searchFind);
            } else {
              array.push([index, "-", "-", "-", "-", "-", "-"]);
            }
          }
          element.array_agg = array;
        });
        return this.tissue;
      }
    },
    getters: {
      async getPlant() {
        console.log("dfsf");
        return this.plant;
      },
    },
  },
});
