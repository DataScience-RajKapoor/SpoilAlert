(function() {
    // Prepend the new fields to the form
    $('#formeo-render').prepend(`
        <div id="custom-fields">
            <label>Adult: </label>
            <input type="radio" id="adult-yes" name="adult" value="yes" checked> Yes
            <input type="radio" id="adult-no" name="adult" value="no"> No

            <br><label>Treatment: </label>
            <input type="radio" id="treatment-yes" name="treatment" value="yes"> Yes
            <input type="radio" id="treatment-no" name="treatment" value="no" checked> No

            <br><label>Insurance Verified: </label>
            <input type="radio" id="insurance-yes" name="insurance" value="yes"> Yes
            <input type="radio" id="insurance-no" name="insurance" value="no" checked> No

            <br><label>New Patient: </label>
            <input type="radio" id="new-patient-yes" name="new-patient" value="yes"> Yes
            <input type="radio" id="new-patient-no" name="new-patient" value="no" checked> No
        </div>
    `);

    // Functions to hide or show specific divs
    function hideDivs(divIds) {
        divIds.forEach(function(id) {
            $('#' + id).hide();
        });
    }

    function showDivs(divIds) {
        divIds.forEach(function(id) {
            $('#' + id).show();
        });
    }

    // Define the divs to hide and show based on Adult
    const adultNoHideDivs = [
        'f-a10ecf0b-a7dd-4de3-b191-81466b5e49a8',
        'f-f46b3771-9d44-4895-9ac0-570929e8614f',
        'f-8f413f85-5cc4-4103-a497-70d8c72656fa',
        'f-725c3778-33b6-4296-bf12-616eae596497',
        'f-344b0ad3-b202-4c5a-bfd5-ab52788684ad',
        'f-2c4c6be9-a7b2-46d5-8a60-b4ae6ea23272',
        'f-933148c9-bb78-41ec-832f-1f728c71ac84',
        'f-9cdb5b2f-4bc6-44cf-b60d-0f760774abc0'
    ];

    const adultYesHideDivs = ['f-03eed97c-6c6d-4745-bc0f-ad592b170c8f', 'f-f2efe510-87c7-4b8a-86a6-c31bbe33e391', 'f-25e579ca-9cec-44d7-a408-948092430351'];

    // Define divs for Insurance Verified
    const insuranceYesHideDivs = [
        'f-2746ea53-8be9-4285-a9b5-f6241660606d',
        'f-d693c65e-b40a-4546-99cb-9af6203b456d',
        'f-9d27f7a6-d28b-418d-ac23-82e56fe3e3ae',
        'f-6c6703da-d147-4b29-9f1a-92bbbfb3b079',
        'f-196db9f2-18bb-4169-904e-2fe81822079e',
        'f-e03efe28-b215-49cb-97ea-513ebf8c0061',
        'f-218281ee-b53c-45e3-b5eb-c083af8ab021',
        'f-de969c15-b7bd-4d23-805c-329c21e0e3c7'
    ];

    const insuranceYesShowDivs = [
        'f-678f5bdf-0da8-4429-b4c3-01d248c75ca4',
        'f-44f87b35-2e2d-48b5-bf09-49dba0814754',
        'f-cf2b2aca-fee2-4a5e-b01a-3a0b64de83d7',
        'f-1efd0dda-afe3-45bc-bbcc-7d98f31c7ed3',
        'f-9cdb5b2f-4bc6-44cf-b60d-0f760774abc0'
    ];

    // Event listener for Adult radio group
    $('input[name="adult"]').on('change', function() {
        if (this.value === 'no') {
            hideDivs(adultNoHideDivs);
        } else {
            hideDivs(adultYesHideDivs);
        }
    });

    // Event listener for Insurance Verified
    $('input[name="insurance"]').on('change', function() {
        if (this.value === 'yes') {
            hideDivs(insuranceYesHideDivs);
            showDivs(insuranceYesShowDivs);
        } else {
            showDivs(insuranceYesHideDivs); // If insurance is not verified, we show the hidden divs back
            hideDivs(insuranceYesShowDivs); // Hide those we show when verified
        }
    });

    // Initialize the form logic for the default selected options
    $('input[name="adult"]:checked').trigger('change');
    $('input[name="insurance"]:checked').trigger('change');
})();
