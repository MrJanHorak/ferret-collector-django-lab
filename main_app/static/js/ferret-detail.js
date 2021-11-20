const dateInput = document.getElementById("id_date");

const picker = MCDatepicker.create({
  el: "#id_date",
  theme: {
    theme_color: "#c7b182",
  },
  dateFormat: "yyyy-mm-dd",
  closeOnBlur: true,
  selectedDate: new Date(),
});

dateInput.addEventListener("click", (evt) => {
  picker.open();
});
