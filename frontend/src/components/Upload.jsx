import { useState } from "react";
import { Button, Modal } from "semantic-ui-react";
import { upload } from "../data/upload";

const Upload = () => {
  const formData = new FormData();

  const handleSubmit = (e) => {
    e.preventDefault();
    const uploadProfile = async () => {
      const res = await upload();
      console.log(res.url);
    };
    uploadProfile();
  };
  const [open, setOpen] = useState(false);

  return (
    <Modal
      onClose={() => setOpen(false)}
      onOpen={() => setOpen(true)}
      open={open}
      trigger={<Button>Show Modal</Button>}
    >
      <Modal.Header>Select a Photo</Modal.Header>
      <Modal.Content image>
        <form onSubmit={handleSubmit}>
          <input type="file" />
          <button type="submit">Submit</button>
        </form>
      </Modal.Content>
      <Modal.Actions>
        <Button color="black" onClick={() => setOpen(false)}>
          Nope
        </Button>
        <Button
          content="Yep, that's me"
          labelPosition="right"
          icon="checkmark"
          onClick={() => setOpen(false)}
          positive
        />
      </Modal.Actions>
    </Modal>
  );
};

export default Upload;
