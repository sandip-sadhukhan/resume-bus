import {
  Flex,
  Heading,
  HStack,
  IconButton,
  Image,
  Text,
  VStack,
} from "@chakra-ui/react"
import Link from "next/link"
import React from "react"
import { BsArrowRight } from "react-icons/bs"
import { FaEye } from "react-icons/fa"

interface BlogGridProps {
  grayBackground: string
  secondaryColor: string
  bannerImg: string
  viewCount: number
  title: string
  date: string
  category: string
  categoryLink: string
  description: string
}

const BlogGrid: React.FC<BlogGridProps> = (props: BlogGridProps) => {
  const {
    grayBackground,
    secondaryColor,
    bannerImg,
    viewCount,
    title,
    date,
    category,
    categoryLink,
    description,
  } = props

  return (
    <VStack shadow="lg" bgColor={grayBackground} w="full">
      <Link href="#">
        <a>
          <Flex
            flexDir="column"
            pos="relative"
            alignItems="center"
            justifyContent="center"
          >
            <HStack
              pos="absolute"
              px={4}
              py={2}
              top={5}
              right={4}
              bgColor={secondaryColor}
              color="white"
            >
              <FaEye />
              <Text>{viewCount}</Text>
            </HStack>
            <Image src={bannerImg} alt={title} />
            <IconButton
              w={10}
              bgColor="white"
              color="black"
              _hover={{ backgroundColor: secondaryColor, color: "white" }}
              aria-label="Arrow"
              icon={<BsArrowRight />}
              zIndex={10}
              rounded="full"
              mt={-4}
            />
          </Flex>
        </a>
      </Link>
      <VStack flex={1} pt={3} pb={6} px={[3, 5, 5, 10, 10]}>
        <Heading as="h6" size="sm">
          {title}
        </Heading>
        <Text fontSize={12}>
          {date} - In{" "}
          <Link href={categoryLink}>
            <a>{category}</a>
          </Link>
        </Text>
        <Text fontSize={14} pt={2} style={{ textAlign: "center" }}>
          {description}
        </Text>
      </VStack>
    </VStack>
  )
}

export default BlogGrid
