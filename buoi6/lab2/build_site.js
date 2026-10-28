const fs = require('fs');
const path = require('path');

const config = require('./docusaurus.config.js');
const buildDir = path.join(__dirname, 'build');

if (!fs.existsSync(buildDir)) {
    fs.mkdirSync(buildDir, { recursive: true });
}

// Generate static index.html
const htmlContent = `<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${config.title}</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 2rem; background: #1a1a2e; color: #e6e6e6; }
        header { text-align: center; padding: 2rem 0; border-bottom: 1px solid #333; }
        h1 { color: #00d2d3; margin-bottom: 0.5rem; }
        .tagline { color: #8395a7; font-size: 1.2rem; }
        .card { background: #22223b; padding: 1.5rem; border-radius: 8px; margin: 1.5rem auto; max-width: 700px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
        .badge { display: inline-block; padding: 0.25rem 0.5rem; border-radius: 4px; font-size: 0.85rem; font-weight: bold; background: #10ac84; color: white; margin-right: 0.5rem; }
        a { color: #54a0ff; text-decoration: none; }
    </style>
</head>
<body>
    <header>
        <h1>${config.title}</h1>
        <p class="tagline">${config.tagline}</p>
        <span class="badge">GitLab Pages</span>
        <span class="badge">DevSecOps Verified</span>
    </header>
    <div class="card">
        <h2>Thông tin Dự án & Triển khai</h2>
        <p><strong>Sinh viên thực hiện:</strong> Nguyễn Nhật Lâm (MSSV: 2387700036)</p>
        <p><strong>Cấu hình URL:</strong> <a href="${config.url}${config.baseUrl}">${config.url}${config.baseUrl}</a></p>
        <p><strong>Quy trình CI/CD:</strong> Build Image Node -> DevSecOps Security Gate -> Deploy GitLab Pages</p>
    </div>
</body>
</html>`;

fs.writeFileSync(path.join(buildDir, 'index.html'), htmlContent, 'utf-8');
console.log(`[Docusaurus] Site successfully built to ${buildDir}/`);
