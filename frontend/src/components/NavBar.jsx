import { Link, useLocation } from "react-router-dom";
import { Menu, Header, Segment, Button } from "semantic-ui-react";

const NavBar = () => {
  const { pathname } = useLocation();
  return (
    <Segment inverted style={{ borderRadius: "0px" }}>
      <Menu inverted pointing secondary size="huge">
        <Header
          as="h1"
          style={{
            color: "white",
            margin: "0px 0px 0px",
            lineHeight: "4rem",
          }}
        >
          Step by Step
        </Header>
        <Menu.Menu position="right">
          <Menu.Item as={Link} to="/" name="home" active={pathname === "/"} />
          <Menu.Item
            as={Link}
            to="/profile"
            name="profile"
            active={pathname === "/profile"}
          />
          <Menu.Item as={Link} to="/login" name="login">
            <Button color="blue">Log In/Register</Button>
          </Menu.Item>
        </Menu.Menu>
      </Menu>
    </Segment>
  );
};

export default NavBar;
