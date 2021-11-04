import api from "./index";

export const getPosts = async () => {
  const res = await api.get("/posts");
  return res.data;
};

export const getPost = async (id) => {
  const res = await api.get(`/posts/${id}`);
  return res.data;
};

export const createPost = async (post) => {
  const res = await api.post("/posts");
  return res.data;
};

// export const getPosts = async (req, res) => {
//   const data = await api.put("/posts");
//   return data;
// };

// export const getPosts = async (req, res) => {
//   const data = await api.get("/posts");
//   return data;
// };
