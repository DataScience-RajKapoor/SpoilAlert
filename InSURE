javascript:(function() {
    // Add custom fields for Adult and Treatment
    $('#formeo-render').prepend(`
      <div id="custom-fields" style="padding-bottom: 10px;">
        <label>Adult: </label>
        <input type="radio" id="adult-yes" name="adult" value="yes" checked> Yes
        <input type="radio" id="adult-no" name="adult" value="no"> No
        <br/>
        <label>Treatment: </label>
        <input type="radio" id="treatment-yes" name="treatment" value="yes"> Yes
        <input type="radio" id="treatment-no" name="treatment" value="no" checked> No
        <br/>
        <div id="treatment-types" style="display:none; padding-top: 10px;">
          <label>Select Treatment Types:</label><br/>
          <input type="checkbox" id="restorative" name="treatment-type" value="restorative"> Restorative
          <input type="checkbox" id="perio" name="treatment-type" value="perio"> Perio
          <input type="checkbox" id="oral" name="treatment-type" value="oral"> Oral
          <input type="checkbox" id="major" name="treatment-type" value="major"> Major
          <input type="checkbox" id="invisalign" name="treatment-type" value="invisalign"> Invisalign
        </div>
      </div>
    `);

    // List of treatment divs that should be hidden initially when Adult = No
    const treatmentDivs = [
        '#f-a10ecf0b-a7dd-4de3-b191-81466b5e49a8', '#f-f46b3771-9d44-4895-9ac0-570929e8614f', '#f-8f413f85-5cc4-4103-a497-70d8c72656fa',
        '#f-725c3778-33b6-4296-bf12-616eae596497', '#f-344b0ad3-b202-4c5a-bfd5-ab52788684ad', '#f-2c4c6be9-a7b2-46d5-8a60-b4ae6ea23272',
        '#f-933148c9-bb78-41ec-832f-1f728c71ac84', '#f-f46b3771-9d44-4895-9ac0-570929e8614f', '#f-8f413f85-5cc4-4103-a497-70d8c72656fa'
    ];

    // Divs to hide when Adult = Yes
    const adultYesHiddenDivs = [
        '#f-03eed97c-6c6d-4745-bc0f-ad592b170c8f',
        '#f-f2efe510-87c7-4b8a-86a6-c31bbe33e391'
    ];

    // Function to handle Adult radio button change
    function toggleAdultFields() {
        const isAdult = $('input[name="adult"]:checked').val() === 'yes';
        if (isAdult) {
            // Show all treatment divs for adults
            $(treatmentDivs.join(',')).show();
            // Hide specific divs for Adult = Yes
            $(adultYesHiddenDivs.join(',')).hide();
        } else {
            hideAllTreatments(); // Hide all treatment divs for kids initially
        }
    }

    // Function to show/hide treatment checkboxes
    function toggleTreatmentFields() {
        const treatmentYes = $('input[name="treatment"]:checked').val() === 'yes';
        $('#treatment-types').toggle(treatmentYes);
        if (!treatmentYes) {
            hideAllTreatments(); // Hide all treatments if Treatment is No
        }
    }

    // Function to hide all treatment-related divs
    function hideAllTreatments() {
        // Hide all treatment type divs
        $(treatmentDivs.join(',')).hide();
    }

    // Function to show specific treatment types
    function toggleTreatmentTypeFields() {
        hideAllTreatments(); // Start by hiding all treatments
        if ($('#perio').is(':checked')) {
            $('#f-725c3778-33b6-4296-bf12-616eae596497, #f-344b0ad3-b202-4c5a-bfd5-ab52788684ad').show();
        }
        if ($('#major').is(':checked')) {
            $('#f-de969c15-b7bd-4d23-805c-329c21e0e3c7, #f-2c4c6be9-a7b2-46d5-8a60-b4ae6ea23272, #f-6273f1db-f2f0-4acb-9019-73e05ade13c7, #f-75aee618-d0ca-40c5-a98b-8cc18d7c2d0d, #f-9cdb5b2f-4bc6-44cf-b60d-0f760774abc0, #f-f46b3771-9d44-4895-9ac0-570929e8614f, #f-8f413f85-5cc4-4103-a497-70d8c72656fa').show();
        }
        if ($('#invisalign').is(':checked')) {
            $('#f-3c63107c-745f-4619-a3e3-70cda78983d6').show();
        }
    }

    // Event listeners
    $('input[name="adult"]').on('change', toggleAdultFields);
    $('input[name="treatment"]').on('change', toggleTreatmentFields);
    $('input[name="treatment-type"]').on('change', toggleTreatmentTypeFields);

    // Initial function calls
    toggleAdultFields(); // Handle adult-related fields on page load
})();
