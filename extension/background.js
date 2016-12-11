function handleNavigate(details) {
    if (details.frameId != 0) {
        // we're interested in page navigations, not sub frames
        return;
    }
    $.ajax({
        url: 'http://127.0.0.1:5000/api/site',
        contentType: "application/json",
        type : 'post',
        data: JSON.stringify({
            'url': details.url,
        }),
        dataType: "json",
    }).done(function(){
            console.log("Sent url to server: " + details.url);
        });
    // return {
    //     redirectUrl: "javascript:",
    // }
}

chrome.webNavigation.onBeforeNavigate.addListener(
    handleNavigate,
    {
        'urls': ['<all_urls>']
    },
    // filters
    // extraInfoSpec
    ["blocking"]);