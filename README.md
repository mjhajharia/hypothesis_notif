 ## Hypothesis Notifications with Github Action  

Private Cache files are stored in a separate repository, which is a submodule here. Otherwise, most of the code here is from [h_notify](https://github.com/judell/h_notify) with minor changes. 

Recommendation: Create a cache file first by commenting out `self.server.sendmail(self.sender, [self.recipient], message.as_string())` for emails, or respective lines for other notification Interfaces. This is to ensure that a cache file is created without sending any notifications the first time, which can be especially undesirable if you have many posts under a user/group/tag. 

Possible Improvements: Considering the recommendation above, it would be nice to be able to avoid this problem altogether, this would require searching based on time with params["update_date"] or something like that, I haven't been able to find the exact parameter name in the hypothesis API, and I'm not sure if the hypothesis Python API ports this properly, although it shouldn't be too difficult to add. Then, this can be in sync with the Github Action schedule, so queries will only be for posts created in the last X minutes or so.
