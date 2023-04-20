////////////////////////////////////////////// vote buttons
function voteButtonListener(nid, category) {
  console.log(nid);

  const formData = new FormData();
  formData.append('nid', nid);

  fetch('/vote', {
    method: 'POST',
    body: formData,
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    alert('Vote submitted successfully');

    // disable all other buttons in the same category
    const buttons = document.querySelectorAll(`.vote-btn[data-category="${category}"]`);
    buttons.forEach(button => {
      button.disabled = true;
    });

    // store voted button ID locally
    localStorage.setItem(`voted-${category}`, true);
  })
  .catch(error => {
    console.error('There was an error:', error);
    alert('Vote submission failed');
  });

  // disable this button
  const button = document.querySelector(`.vote-btn[data-nid="${nid}"]`);
  button.disabled = true;
}

// attach event listener to all vote buttons
const voteButtons = document.querySelectorAll('.vote-btn');
voteButtons.forEach(button => {
  const nid = button.dataset.nid;
  const category = button.dataset.category;

  // check if the button has already been voted
  if (localStorage.getItem(`voted-${category}`)) {
    button.disabled = true;
  } else {
    button.addEventListener('click', event => {
      event.preventDefault();
      voteButtonListener(nid, category);
    });
  }
});


////////////////////////////////////////////// admin buttons
function deleteNominee(nid) {
  const formData = new FormData();
  formData.append("nid", nid);

  const request = new Request("/admin", {
    method: "POST",
    body: formData,
  });

  fetch(request)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      console.log("Nominee deleted successfully");
    })
    .catch((error) => {
      console.error("Error deleting nominee:", error);
      // Add code to handle error and update UI as needed
    });
}

const deleteButtons = document.querySelectorAll('.delete-btn');
deleteButtons.forEach((button) => {
  button.addEventListener('click', (event) => {
    // get the nominee ID from the button's data-nid attribute
    const nomineeID = event.target.dataset.nid;

    // call the deleteNominee function with the nominee ID
    deleteNominee(nomineeID);

    // remove the nominee's row from the HTML
    const nomineeRow = event.target.closest('.card');
    nomineeRow.remove();
  });
});


// add new nominee
function addNominee() {
  const name = document.querySelector('input[placeholder="Name"]').value;
  const country = document.querySelector('input[placeholder="Country"]').value;
  const status = document.querySelector('input[placeholder="Status"]').value;
  const music = document.querySelector('input[placeholder="Music"]').value;
  const awardCategory = document.querySelector('input[placeholder="Award Category"]').value;
  const year = document.querySelector('input[placeholder="Year"]').value;

  const formData = new FormData();
  formData.append("name", name);
  formData.append("country", country);
  formData.append("status", status);
  formData.append("music", music);
  formData.append("awardCategory", awardCategory);
  formData.append("year", year);

  const request = new Request("/admin", {
    method: "POST",
    body: formData,
  });

  fetch(request)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      console.log("Nominee added successfully");
    })
    .catch((error) => {
      console.error("Error adding nominee:", error);
    });
}

const addBtn = document.querySelector('.add-btn');
addBtn.addEventListener('click', addNominee);

