import { useEffect, useState } from "react";
import { Item } from "semantic-ui-react";
import Layout from "../components/Layout";
import Post from "../components/Post";
import { getPosts } from "../data/posts";

const Home = () => {
  const [posts, setPosts] = useState([]);
  useEffect(() => {
    const fetchPosts = async () => {
      const posts = await getPosts();
      setPosts(posts);
    };
    fetchPosts();
  }, []);
  return (
    <Layout>
      <Item.Group divided>
        {posts?.map((post, index) => (
          <Post key={index} post={post} />
        ))}
      </Item.Group>
    </Layout>
  );
};

export default Home;
