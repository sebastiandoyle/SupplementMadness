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