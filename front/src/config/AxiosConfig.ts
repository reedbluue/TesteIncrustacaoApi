import axios from "axios";
import { VITE_API_KEY } from "./EnvConfig";

export const baseURL = axios.create({
  baseURL: `${VITE_API_KEY}`,
});