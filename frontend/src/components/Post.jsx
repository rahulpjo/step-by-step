import { Item, Icon, Label } from "semantic-ui-react";
const Post = ({ post }) => {
  const { body, likes, tag, author } = post;
  const { first_name, last_name, img_url } = author;
  return (
    <Item>
      <Item.Image src={img_url} />
      <Item.Content>
        <Item.Header>
          {first_name} {last_name}
        </Item.Header>
        <Item.Meta>
          <Label icon="tag" content={tag} />
        </Item.Meta>
        <Item.Description>{body}</Item.Description>
        <Item.Extra>
          <Icon name="like" />
          {likes} Likes
        </Item.Extra>
      </Item.Content>
    </Item>
  );
};

export default Post;
