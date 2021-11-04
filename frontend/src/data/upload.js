import api from "./index";

export const upload = async (data) => {
  const res = await api.post("/files/upload", data, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
  return res.data;
};
