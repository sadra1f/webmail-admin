function POSTRedirect(attributes, data) {
  const form = document.createElement("form");

  Object.entries(attributes).forEach(([key, value]) => {
    form.setAttribute(key, value);
  });

  Object.entries(data).forEach(([key, value]) => {
    const input = document.createElement("input");

    input.setAttribute("type", "hidden");
    input.setAttribute("name", key);
    input.setAttribute("value", value);

    form.appendChild(input);
  });

  const submit = document.createElement("input");
  submit.setAttribute("type", "submit");
  form.appendChild(submit);

  form.style.display = "none";

  document.body.appendChild(form);
  form.querySelector("input[type='submit']").click();
  document.body.removeChild(form);
}
