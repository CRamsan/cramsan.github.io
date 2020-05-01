---
layout: post
title: Bringing Back Auraxis Control Center
tags: random
categories: other
---

I can't believe that I last updated this app on Sep 16, 2018. But with the release of the escalation update, I decided it was a good time to get back into updating this app. But I not only wanted to fix bugs here and there, I wanted to get back into listening to the community feedback and adding new features.

But in order to achieve some long term goals, I knew I needed to make some changes. Developing this app has taught me so things in the seven years of working on it and a lot of the early mistakes had started to really affect development speed. The lack of unit and integration test allowed regressions to get into the released app and even then, getting information about user crashes was only came from the Play Store. Overall, most of the problems with this app were due to a ver bad development process. This would cause a feedback look, since I was not willing to make bug changes due to the fear of breaking thing. So most of the changes that have been done over the last couple years were ad-hoc changes heavily guarded with null checks.

I wanted to change that, so I wanted to implement the following:
- Add unit tests and UI tests
- Enable a CI/CD mechanism
- Update libraries and tools to their newer versions
- Integrate a mechanism to get crash and diagnostic information
- Add analytics to the app to better understand user behavior

I can happily say that I did achieve all the expected goals. The app now builds using Azure Pipelines and it is published to the Azure App Center with a Debug and Release apps. Unit tests are part of the build pipeline, UI tests are not integrated yet. The Debug app is published for devs and testers to use. While the release app is automatically uploaded to the Play Store's private release channel. 

**Pipelines automatically building on every commit**

<img src="/assets/screenshots/2020-04-30 22-03-53-pipeline.png" class="embeddedElement">

**Realtime time crash data with insights**

<img src="/assets/screenshots/2020-04-30 22-05-38-crashes.png" class="embeddedElement">

Another great milestone was that all the app was migrated to Kotlin. This allowed me to easily integrate with my existing set of core Kotlin libraries. I am using the Azure App Center SDK to collect crash metrics and to get user insights. 

To celebrate all these new changes. I also created a [new website](https://cramsan.com/auraxiscontrolcenter-site/) to send updates about this project. I am pretty happy with the result, but mostly I am excited what the future has in store for us.

Regards,
CRamsan