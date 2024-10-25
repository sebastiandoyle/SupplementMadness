import os

def create_folder_structure():
    # Define the folder structure and files
    structure = {
        "app": {
            "page.js": '''
'use client';
import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';

export default function QuizPage() {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);

  return (
    <main className="min-h-screen p-8">
      <Card className="max-w-2xl mx-auto p-6">
        <h1 className="text-2xl font-bold mb-4">Quiz App</h1>
        {/* Add your quiz content here */}
      </Card>
    </main>
  );
}
''',
            "layout.js": '''
export const metadata = {
  title: 'Quiz Application',
  description: 'Interactive quiz application built with Next.js',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
''',
            "globals.css": '''
@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --foreground-rgb: 0, 0, 0;
  --background-rgb: 255, 255, 255;
}

body {
  color: rgb(var(--foreground-rgb));
  background: rgb(var(--background-rgb));
}
'''
        },
        "components": {
            "ui": {
                "button.jsx": '''
export function Button({ children, ...props }) {
  return (
    <button
      className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
      {...props}
    >
      {children}
    </button>
  );
}
''',
                "card.jsx": '''
export function Card({ children, className, ...props }) {
  return (
    <div
      className={`bg-white rounded-lg shadow ${className}`}
      {...props}
    >
      {children}
    </div>
  );
}
''',
                "badge.jsx": '''
export function Badge({ children, variant = 'default', ...props }) {
  const variants = {
    default: 'bg-gray-100 text-gray-800',
    success: 'bg-green-100 text-green-800',
    error: 'bg-red-100 text-red-800',
  };

  return (
    <span
      className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${variants[variant]}`}
      {...props}
    >
      {children}
    </span>
  );
}
'''
            }
        }
    }
    
    # Configuration files in root directory
    root_files = {
        "package.json": '''{
  "name": "quiz-app",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "14.0.0",
    "react": "^18",
    "react-dom": "^18"
  },
  "devDependencies": {
    "autoprefixer": "^10",
    "postcss": "^8",
    "tailwindcss": "^3"
  }
}''',
        "tailwind.config.js": '''/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}''',
        "postcss.config.js": '''module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}'''
    }

    def create_files(curr_path, structure):
        for name, content in structure.items():
            path = os.path.join(curr_path, name)
            if isinstance(content, dict):
                # If it's a dictionary, it's a directory
                os.makedirs(path, exist_ok=True)
                create_files(path, content)
            else:
                # If it's not a dictionary, it's a file
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content.strip())

    # Create the directory structure and files in current directory
    create_files(".", structure)
    
    # Create root configuration files
    for filename, content in root_files.items():
        filepath = os.path.join(".", filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content.strip())
    
    print("Project structure created successfully in the current directory!")

if __name__ == "__main__":
    create_folder_structure()
