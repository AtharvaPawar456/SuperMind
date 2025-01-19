document.addEventListener("DOMContentLoaded", function () {
  // function addNewEvent(info) {
  //   formEvent.classList.remove("was-validated");
  //   formEvent.reset();
  //   selectedEvent = null;
  //   modalTitle.innerText = "Add Event";
  //   newEventData = info;
  // }

  const calendarEl = document.getElementById("calendar");
  const formEvent = document.getElementById("form-event");
  const eventModal = document.getElementById("event-modal");
  const eventTitleInput = document.getElementById("event-title");
  const eventCategoryInput = document.getElementById("event-category");
  const deleteEventBtn = document.getElementById("btn-delete-event");
  const saveEventBtn = document.getElementById("btn-save-event");
  const eventModalCloseBtn = document.getElementById("eventModal-close");

  // console.log(eventForm.elements);

  const calendar = new FullCalendar.Calendar(calendarEl, {
    timeZone: "UTC",
    editable: true,
    droppable: true,
    selectable: true,
    selectMirror: true,
    // initialDate: "2021-02-13",
    // weekNumbers: true,
    // navLinks: true,
    nowIndicator: true,

    // themeSystem: "tailwindcss",

    headerToolbar: {
      left: "prev,next,today",
      center: "title",
      right: "dayGridMonth,timeGridWeek,timeGridDay,listMonth",
    },

    // select: function (arg) {
    //   var title = prompt("Event Title:");
    //   if (title) {
    //     calendar.addEvent({
    //       title: title,
    //       start: arg.start,
    //       end: arg.end,
    //       allDay: arg.allDay,
    //     });
    //   }
    //   // calendar.unselect();
    // },
    dateClick: function (info) {
      // addNewEvent(info);
      console.log(info);
      document.getElementById("event-button").click();

      // calendar.addEvent({
      // title: title,
      // start: arg.start,
      // end: arg.end,
      // allDay: arg.allDay,
      // });
    },
    events: [
      {
        title: "All Day Event",
        start: "2024-06-10",
      },
      {
        title: "Long Event",
        start: "2021-02-07",
        end: "2021-02-10",
        className: "bg-danger",
      },
      {
        groupId: 999,
        title: "Repeating Event",
        start: "2021-02-09T16:00:00",
      },
      {
        groupId: 999,
        title: "Repeating Event",
        start: "2021-02-16T16:00:00",
      },
      {
        title: "Conference",
        start: "2021-02-11",
        end: "2021-02-13",
        className: "bg-danger",
      },
      {
        title: "Lunch",
        start: "2021-02-12T12:00:00",
      },
      {
        title: "Meeting",
        start: "2021-04-12T14:30:00",
      },
      {
        title: "Happy Hour",
        start: "2021-07-12T17:30:00",
      },
      {
        title: "Dinner",
        start: "2021-02-12T20:00:00",
        className: "bg-warning",
      },
      {
        title: "Birthday Party",
        start: "2021-02-13T07:00:00",
        className: "bg-secondary",
      },
      {
        title: "Click for Google",
        url: "http://google.com/",
        start: "2021-02-28",
      },
    ],
    // windowResize: function () {
    //     const newView = getInitialView();
    //     calendar.changeView(newView);
    // },
    // eventDidMount: function (info) {
    //     if (info.event.extendedProps.status === 'done') {
    //         info.el.style.backgroundColor = 'red';
    //         const dotEl = info.el.querySelector('.fc-event-dot');
    //         if (dotEl) {
    //             dotEl.style.backgroundColor = 'white';
    //         }
    //     }
    // },
    // eventClick: function (info) {
    //     document.getElementById("event-button").click();
    //     document.getElementById("event-modal").classList.remove('hidden');
    //     formEvent.reset();
    //     document.getElementById("event-title").value = "";
    //     selectedEvent = info.event;
    //     document.getElementById("event-title").value = selectedEvent.title;
    //     document.getElementById('event-category').value = selectedEvent.classNames[0];
    //     newEventData = null;
    //     document.getElementById('btn-delete-event').classList.remove("hidden");
    //     document.getElementById('btn-save-event').innerText = 'Edit Event';
    //     newEventData = null;
    // },

    // events: defaultEvents
  });
  calendar.render();
});
