<h1>Scientific Paper Keywords Categorization</h1>

<h2>Project Development Journal</h2>

<h3><code style="color:blue">Problem Statement</code></h3>
<strong></strong>

<h3><code style="color:blue">Objective</code></h3>
<strong>Keywords is a necessary part of a scientific paper. It helps search engines to show papers to users based on relatable topics. So, choosing these words properly is really important. The goal here now is to create a developed and optimized keyword categorizer that can classify a scientific paper between particular keywords based on the abstrat of the paper. </strong>

<h3><code style="color:blue">Data Collection</code></h3>
<strong> I collected data for the open access papers. IEEE doesn't provide more than    
    To execute the collection process, I firstly created scrapers using selenium after inspecting the website. It doesn't provide  As I needed the abstract and the available keywords for that paper (including both IEEE and author), . </strong>

<h3><code style="color:blue">Data Pre-processing</code></h3>

<h3><code style="color:blue">Model Experimentations</code></h3>

<h3><code style="color:blue">Model Evaluation</code></h3>

<h3><code style="color:blue">Model Compression</code></h3>

<h3><code style="color:blue">Deployment</code></h3>
<div align="center">
    <img src="readmeFileImages/deployment.png">
</div>

<h3><code style="color:blue">Integration to website</code></h3>
<strong>I integrated the model <a href="https://render.com/">render</a>. Check out the live website <a href="https://scientific-paper-keywords-categorization.onrender.com/">here</a>.</strong><br/>

<div align="center">
    <table>
        <tr>
            <th>Home Page</th>
            <th>Prediction Result</th>
        </tr>
         <tr>
            <td><img src="readmeFileImages/1st_page.png" height="300"></td>
            <td><img src="readmeFileImages/2nd_page.png" height="300"></td>
        </tr>
    </table>
</div>

<h3><code style="color:blue">Challenges Faced</code></h3>
<ul>
    <li>
        <strong>After a scraper script runs for a long time, sometimes it shows "Aw, Snap!" message in the running chrome. In that case, I just reloaded the webpage mannually and then it started working properly as previous.</strong><br/>
        <img src="readmeFileImages/aw_snap.png" width="300" height="150"><br/>
    </li>
    <li><strong>The required webelements distribution in all webpages wasn't the same. For some webpages, the scraper collecting details were working fine but it showed exceptions for those. So, I had to re-write some codes considering the different ones and generalize the codes.</strong></li>
    <li><strong>As I had to collect a lot of data, so, I created same type of scrapers and running them simultaneously from different indexes. It boosted my data collection process a bit although it depended much on internet speed.</strong></li>
    <li><strong>In the end, it took huge time to collect a desirable amount of data. So, I had to wait with patience.</strong></li>
    <li><strong>Some abstracts contains values like "Retracted.", "Final version", "IEEE Plagarism Policy." and some more unconsiderable values. So, I went through the whole dataset and found these values mannually for the data cleaning process.</strong></li>
</ul>
